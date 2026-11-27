export async function fetch_request(addr: string, method: string = "GET", credentials: bool = false, body?: Record<string, unknown>) {
	let url = "http://localhost:8000"
		
	let credentials_ = credentials ? "include" : "same-origin"
	return fetch(url+addr, {
		method: method,
		headers: { "Content-Type" : "application/json" },
		credentials: credentials_,	
		...(body && method.toUpperCase() !== "GET" ? {body: JSON.stringify(body)} : {}),
	})
} 
