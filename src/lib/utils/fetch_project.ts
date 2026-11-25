export interface ProjectPayload{
	project_id:string
}

export async function fetchProject(payload:ProjectPayload) {
	try {
		console.log(payload)
		const res: Response = await fetch("http://localhost:8000/projects/fetch-one", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			credentials: "include",
			body: JSON.stringify({ "project_id" : payload.project_id})
		})

		const data = await res.json().catch(() => null)

		return data.message
	} catch(err) {
		console.log(err)
	}
}
