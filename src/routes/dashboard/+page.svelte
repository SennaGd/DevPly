<script lang="ts">
	import { onMount } from 'svelte';
	import { auth } from '#lib/auth.svelte.js';
    import { goto } from '$app/navigation';

	let username = $state("")
	onMount(async () => {
			const res: Response = await fetch("http://localhost:8000/user", {
				credentials: "include"
			})

			if ( res.ok ) {
				const data = await res.json();
				username = data.id;
			}
		})
</script>

<p>{auth.responseStatus}</p>
{username}
