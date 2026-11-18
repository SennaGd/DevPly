<script lang="ts">
	import { onMount } from 'svelte';
	import { auth } from '#lib/auth.svelte.js';
    import { goto } from '$app/navigation';

	interface RolesResponse {
		message: Record<number, string>
	}
	
	interface RoleItem {
		id: number
		role: string
	}

	let roleArr = $state<RoleItem[]>([]) 
	let username = $state("")
	let userId = 0
	let roleId = 0
	let user_role = $state("")

	let title= $state("")
	let desc= $state("")
	
	onMount(async () => {
		let res: Response = await fetch("http://localhost:8000/user", {
			credentials: "include"
		})

		if ( res.ok ) {
			const data = await res.json();
			username = data.username
			roleId = data.role_id-1 // role_id = -1 python > sql indices
			userId = data.id
		}

		const roles: Response = await fetch("http://localhost:8000/roles")
		if ( roles.ok ) {
			const data: RolesResponse = await roles.json()
			console.log(data)

			roleArr = Object.entries(data.message)
							.map(([id,role]) => ({
								id: Number(id),	
								role
							}))
			user_role = Object.entries(data.message)[roleId][1]
		}
		let projectResult: Response = await fetch("http://localhost:8000/fetch_projects", {
			method: "GET",
			headers: { "Content-Type": "application/json"},
			credentials: "include"
		})
		if (res.ok) {
			const projectsData= await projectResult.json()
				console.log(Object.entries(projectsData.message)[0][1])

		}
		console.log(res)
	})
	async function create_project() {
		console.log("h")
		try {
			const creator_id = userId
			const res: Response = await fetch("http://localhost:8000/create_project", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify({ title:title, description:desc, creator_id})
			})

			if (!res.ok) {
				console.log("request failed")
			}

			console.log(res)

		} catch(err) {

		} finally {
			const res: Response = await fetch("http://localhost:8000/fetch_projects", {
				method: "GET",
				headers: { "Content-Type": "application/json"},
				credentials: "include"
			})
		}
	}
</script>

<div>
	<p>Your username is '<b>{username}</b>' and you are a '<b>{user_role}</b>'</p>

	{#if user_role == "admin"}
		admin
	{:else}
		normal user	
	{/if}

	<br/>

	<form onsubmit={create_project}>
		<input bind:value={title} required type="text"/><br/>
		<input bind:value={desc} required type="text"/><br/>

		<input type="submit"/>

	</form>

	
</div>

