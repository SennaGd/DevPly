<script lang="ts">
	import { createAccount } from '#lib/utils/auth/create_account.ts'
	import { loginRequest } from '#lib/utils/auth/login.ts'

	let username = $state("")
	let password = $state("")
	let email = $state("")
	let role_id = 0
	
	async function handleCreateAccount(event: SubmitEvent) {
		event.preventDefault()

		await createAccount({
			username, email, password, role_id
		})
	}
	
	async function handleLoginRequest(event: SubmitEvent) {
		event.preventDefault()

		await loginRequest({
			username, password
		})
	}

</script>

<!-- login -->
<form method="POST" onsubmit={handleLoginRequest}>
	<label>username</label><br/>
	<input bind:value={username} required type="text"/><br/>
	<label>email</label><br/>
	<input bind:value={email} type="text"/><br/>
	<label>password</label><br/>
	<input bind:value={password} required type="password"/><br/>
	<input value="login" type="submit"/>
</form>


<!-- register new user -->
<form onsubmit={handleCreateAccount}>
	<input value="create account" type="submit"/>
</form>


