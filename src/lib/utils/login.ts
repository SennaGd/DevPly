// 
import { goto } from '$app/navigation';

export interface LoginPayload {
	username: string
	password: string
}

export async function loginRequest(payload: LoginPayload) {
	try {
		const res = await fetch(`http://localhost:8000/login`, {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			credentials: "include",
			body: JSON.stringify( payload ) 
		})

		if (!res.ok)
		{ return {"Message":"Failed"} }

		if ( res.status == 200 ) {
			console.log("logged in!")
			goto("/dashboard")
		}

	} catch(err) {
		console.log(err)
		return {"Message":err}
	}
}
