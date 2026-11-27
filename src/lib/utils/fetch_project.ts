import { fetch_request } from "#lib/core/fetch.ts";
export interface ProjectPayload{
	project_id:string
}


export async function fetchProject(payload: ProjectPayload) {
	try {
		const res = await fetch_request("/projects/fetch_one", "POST", true , {"project_id":"1"})
		const data = await res.json()

		console.log("data", data.message)
	} catch(err) {
		console.log(err)
	}
}
