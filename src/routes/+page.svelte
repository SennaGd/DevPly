<script lang="ts">
	import { setContext } from 'svelte';
	import { auth } from '#lib/auth.svelte.js';
    import { goto } from '$app/navigation';

	let username = $state("")
	let password = $state("")
	let email = $state("")

	let responseStatus = $state(404)

	async function createAccount(event: SubmitEvent) {
		event.preventDefault()	

		try {
			const response = await fetch(`http://localhost:8000/register`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify({ username, email, password })
			})

			console.log(response)
		} catch (err) {

		} finally {

		}

	}
	async function login(event: SubmitEvent){
		event.preventDefault()

		try {
			const response = await fetch(`http://localhost:8000/login`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify({ username, password })
			})
			if (!response.ok)
			{ return }

			auth.responseStatus = response.status

		} catch(err) {
			console.log(err)
		} finally {
			console.log("status",responseStatus)
			if (auth.responseStatus == 200) {
				await goto("/dashboard")
			}
		}
	}	
</script>

<p>Response Status: {responseStatus}</p>
<form method="POST" onsubmit={login}>
	<input bind:value={username} required type="text"/><br/>
	<input bind:value={password} required type="password"/><br/>
	<input type="submit"/>
</form>

<form method="POST" onsubmit={createAccount}>
	<input bind:value={username} required type="text"/><br/>
	<input bind:value={email} required type="text"/><br/>

	<input bind:value={password} required type="password"/><br/>
	<input type="submit"/>

</form>

