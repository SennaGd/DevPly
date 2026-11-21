export function load({ params }) {
	// params.id matches the folder name [id]
	return {
		projectId: params.id
		// Usually you'd fetch data here, e.g.:
		// project: await getProjectById(params.id)
	};
}
