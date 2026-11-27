<script lang="ts">
	import { onMount } from 'svelte';
	import { createProject } from "#lib/utils/create_project.ts"
	import { getProjects } from "#lib/utils/fetch_projects.ts"
    import { getUser } from '#lib/utils/get_user.ts';

	interface Project {
		id: number
		title: string
		description: string
		creator_id: number
		created_time: string
	}

	interface ProjectsResponse {
		message: Record<number, Project[]>
	}

	let projectData = $state<ProjectsResponse|null>(null)
	async function handleFetchProjects(event?: SubmitEvent) {
		if ( event ) { event.preventDefault() } 

		const res = await getProjects()
		if (res != null && res.ok) {
			projectData = await res.json()
		}
	}

	let username = $state("")
	let userId = 0
	onMount(async () => {
		let res = await getUser()
		if ( res && res.ok) {
			const data = await res.json();
			username = data.username
			userId = data.id
		}
		handleFetchProjects()
	})
	
	// variables from form
	let title= $state("")
	let desc= $state("")
	async function handleCreateProject(event: SubmitEvent) {
		event.preventDefault()
		if (userId != 0) {
			await createProject({ title:title, description:desc,creator_id:userId })
			handleFetchProjects()
		}
	}
</script>

<div>
	<p>Your username is '<b>{username}</b>' </p>
	<br/>

	<form onsubmit={handleCreateProject}>
		<input bind:value={title} required type="text"/><br/>
		<input bind:value={desc} required type="text"/><br/>

		<input type="submit"/>

	</form>
	<br/>
	<h1>Projects</h1>
	{#if projectData?.message}
		{#each projectData.message as [id, title, description, creator_id, created_time] (id)}
		<div>
			<h3>Project: {title}</h3>
			<p>Description: {description}</p>
			<small>Created by user {creator_id} at {created_time}</small>
			<a href="/project/{id}">{title}</a>
		</div>
	{/each}
{/if}
	
</div>

