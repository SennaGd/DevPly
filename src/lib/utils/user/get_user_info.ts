import { fetch_request } from "#lib/core/fetch.ts"

export async function getUser() {
	try {
		const res = await fetch_request("/users/info", "GET", true)	
		if (res.ok) {
			return res 
		}

	} catch (err) {
		console.log("Request failed")
		return null
	}
}
