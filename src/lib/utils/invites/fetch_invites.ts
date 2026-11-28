// fetches users invites 
import { fetch_request } from "#lib/core/fetch.ts";
export async function fetchInvites() {
	try {
		let res = await fetch_request("/invites/get/all", "GET", true)	
		const data = await res.json()
		
		return data.message
	} catch (err) {
		console.log(err)
	}
}
