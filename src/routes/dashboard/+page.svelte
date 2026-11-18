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
	let role_id = 0
	let user_role = $state("")
	onMount(async () => {
			const res: Response = await fetch("http://localhost:8000/user", {
				credentials: "include"
			})

			if ( res.ok ) {
				const data = await res.json();
				username = data.username
				role_id = data.role_id-1 // role_id = -1 python > sql indices

			}

			const roles: Response = await fetch("http://localhost:8000/roles")
			if ( roles.ok ) {
				const data: RolesResponse = await roles.json()
				console.log(data)

				roleArr = Object.entries(data.message)
							.map(([id,role]) => ({
								id: Number(id),	role
							}))

				user_role = Object.entries(data.message)[role_id][1] 			}

		})
</script>

<p>{auth.responseStatus}</p>
your username is '<b>{username}</b>' and you are a '<b>{user_role}</b>'

