<script>
	let username = "";

	async function handleSubmit(event) {
		event.preventDefault()
		const response = await fetch(`http://localhost:8000/user/${encodeURIComponent(username)}`)
		if (!response.ok) {
			console.error("Request failed:", response.status);
			return;
		}

		const result = await response.json();
		console.log(result);
	}	
</script>

<form method="POST" onsubmit={handleSubmit}>
	<input bind:value={username} required type="text"/>
	<input type="submit"/>
</form>
