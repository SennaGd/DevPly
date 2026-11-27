export async interface ProjectUsersPayload {
	project_id: string
	creator_id: string
}

export async function getProjectsUser(payload: ProjectUsersPayload) {
	try {
		const res: Response = await fetch("http://localhost:8000/projects/fetch-one", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			credentials: "include",
			body: JSON.stringify({ "project_id" : payload.project_id})
		})
	} catch(err) {

	}
})
	 
