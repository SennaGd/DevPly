	async function create_project() {
		try {
			const res: Response = await fetch("http://localhost:8000/create_project", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify({ title:title, description:desc })
			})

			if (!res.ok) {
				console.log("request failed")
			}

		} catch(err) {

		} finally {
			const res: Response = await fetch("http://localhost:8000/fetch_projects", {
				method: "GET",
				headers: { "Content-Type": "application/json"},
				credentials: "include"
			})
		}
	}

export interface NewProjectPayload {
	title: string 
	description: string
}

export async function createProject(payload: NewProjectPayload) {
	console.log(payload.title)
	try {
		const res: Response = await fetch("http://localhost:8000/create_project", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			credentials: "include",
			body: JSON.stringify({ title:payload.title, description:payload.description })
		})

		if (!res.ok) {
			return {"Message": "Failed"}
		} else {
			return {"Message": "Success"}
		}
	} catch(err) {
		return {"Message": err}
	} 
}
