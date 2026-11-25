export interface RegisterPayload {
	username: string
	email: string
	password: string
	role_id: number 
}

export async function createAccount(payload: RegisterPayload) {
	console.log(payload)
	try { const response = await fetch("http://localhost:8000/register", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(payload)

		})

		const data = await response.json().catch(() => null)

		if (!response.ok) {
			console.log("Failed to create account, reason:", response)
		}

	} catch (err) {
		console.log("Error creating user ", err)
	} 
}
