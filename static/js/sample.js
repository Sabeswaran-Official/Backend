function GetData(){
    fetch('http://localhost:8000/student/task/api')

    .then(Response=> Response.json())
    .then(data=> console.log(data))
    .then(error=> console.log(error))
    
}

function CreateData(){
    fetch('http://localhost:8000/student/task/api/',{
        method : 'POST',
        headers:{
            'Content-Type':'application/json',
            // "Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyNTgzNTg4LCJpYXQiOjE3NTI1ODE3ODgsImp0aSI6IjA0ZmIwMDVmYzg0MzRiOTBiNTAxNzc3NTVmYzQ4M2I2IiwidXNlcl9pZCI6MX0.azlkyMLJRv1beCKucLjJK_09pKvt7btTdtmj56qZfwY"
        },
        body : JSON.stringify({
            student_reference:1,
            task_name:"Project",
            description:"Using Django"
        })
    })
    .then(Response=> Response.json())
    .then(data=> console.log(data))
    .then(error=> console.log(error))
}

function UpdateData(){
    fetch('http://localhost:8000/student/task/api/3/',{
        method : 'PATCH',
        headers:{
            'Content-Type':'application/json',
        },
        body : JSON.stringify({
            student_reference:1,
            task_name:"Project",
            description:"Using Django_REST framework"
        })
    })
    .then(Response=> Response.json())
    .then(data=> console.log(data))
    .then(error=> console.log(error))
}

function DeleteData(){
    fetch('http://localhost:8000/student/task/api/3/', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(Response=> Response.json())
    .then(data=> console.log(data))
    .then(error=> console.log(error))
}

function StudData(){
    fetch('http://localhost:8000/student/api')

    .then(Response=> Response.json())
    .then(data=> console.log(data))
    .then(error=> console.log(error))
}