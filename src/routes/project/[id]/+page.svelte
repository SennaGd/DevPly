<script lang="ts">
	import { fetchProject } from "#lib/utils/fetch_project.ts"
    import { onMount } from "svelte";

	let { data } = $props();
	let project_id = $state("")	
	let project = $state([])

	console.log(data.projectId)

	if ( data.projectId ) {
		project_id = data.projectId
	} 
		
	onMount(async () => { 
		project = await fetchProject({project_id})
	} )

	async function createRequirement()	{
		

	}
</script>

{project[1]} <br/>
{project[2]}

<form>
	<br/>
	<input type="label"/>	<br/>
	<br/>
	<input type="label"/>	<br/>


	<input type="submit" onsubmit={createRequirement}/>
</form>
