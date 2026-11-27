import { fetch_request } from "#lib/core/fetch.ts";

export interface RegisterPayload {
	username: string
	email: string
	password: string
	role_id: number 
}

export async function createAccount(payload: RegisterPayload) {
	console.log(payload)
	try { 
		const res = await fetch_request("/users/register", "POST", false, payload)
		const data = await response.json().catch(() => null)

		if (!response.ok) {
			console.log("Failed to create account, reason:", response)
		}
	} catch (err) {
		console.log("Error creating user ", err)
	} 
}
