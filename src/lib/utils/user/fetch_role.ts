// Fetches user's role

export interface RolesResponse {
		message: Record<number, string>
	}
	
export interface RoleItem {
		id: number
		role: string
	}

export async function fetchRole() {
	const res: Response = await fetch("http://localhost:8000/roles")
		if ( res.ok ) {
			const data: RolesResponse = await res.json()

			let roleArr = Object.entries(data.message)
							.map(([id,role]) => ({
								id: Number(id),	
								role
							}))
			user_role = Object.entries(data.message)[roleId][1]
		}
} 

