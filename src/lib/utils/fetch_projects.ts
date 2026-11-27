import { fetch_request } from "#lib/core/fetch.ts"

export async function getProjects() {
	try {
		const res = await fetch_request("/projects/fetch_all", "GET", true)
		return res 
	} catch (err) {
		console.log("Request failed", err)
		return null
	}	
}
