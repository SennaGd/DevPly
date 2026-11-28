import { fetch_request } from "#lib/core/fetch.ts";

export interface NewProjectPayload {
	title: string 
	description: string
	creator_id: number
}

export async function createProject(payload: NewProjectPayload) {
	try {
		const res = await fetch_request(
			"/projects/create", "POST", true, payload
		)

		if (!res.ok) {
			console.log("request failed")
		}
	} catch(err) {
		console.log(err)
	} 
}
