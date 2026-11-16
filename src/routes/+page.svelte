<script>
	let username = $state("");
	let password = $state("");
	let errorMessage = $state("");
	let isLoading = $state(false);
	async function handleSubmit(event) {
		event.preventDefault()
		errorMessage = "";
		isLoading = true;
		try {
			const response = await fetch(`http://localhost:8000/login`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify({ username, password })
			})


			console.log(response)
			if (!response.ok) {
				console.error("Request failed:", response.status);
				return;
			}
			
			const result = await response.json();
			console.log(result);
			console.log(document.cookie.split('; '))
		} catch(err) {
			console.log(err)
		} finally {
			isLoading = false
		}
	}	
	let user = $state("")
</script>

<form method="POST" onsubmit={handleSubmit}>
	<input bind:value={username} required type="text"/><br/>
	<input bind:value={password} required type="text"/><br/>
	<input type="submit"/>
</form>

<p></p>
