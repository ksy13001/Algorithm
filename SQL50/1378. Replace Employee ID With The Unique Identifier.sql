select eu.unique_id, ep.name from Employees ep
left outer join EmployeeUNI eu
    on ep.id = eu.id
