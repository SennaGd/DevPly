<script lang="ts">
	import { fetchProject } from "#lib/utils/fetch_project.ts"
    import { onMount } from "svelte";
	let title = $state("")
	let description= $state("")

	let { data } = $props();
	let project_id = $state("")	
	let project = $state([])

	console.log(data.projectId)

	if ( data.projectId ) {
		project_id = data.projectId
	}
		
	onMount(async () => { 
		project = await fetchProject({project_id:project_id})
	} )

	async function createRequirement()	{
		console.log(title, description)	
		
	}
</script>





<br/><br/>
<form onsubmit={createRequirement}>
	<label>
		Requirement Title<br/>
		<input bind:value={title} required type="text"/>
	</label><br/>
	
	<label>
		Description<br/>
		<input bind:value={description} required type="text"/>
	</label><br/>

	<input type="submit"/>
</form>
