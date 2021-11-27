import axios, { Axios } from 'axios'
import {v4 as uuidv4} from 'uuid';


let APIURL = "http://host.docker.internal:8000";

export const createuser = async (e:any) => {
    console.log(e)
    let uuid = uuidv4();
    const { data } = await axios({
      method: 'post',
      url: 'http://localhost:8000/signup/',
      data: {
        username: e['username'],
        password:e['password'],
        password2:e['password2'],
      }
    })
    console.log(data)

    return data
}

export const login = async (e:any) => {
  const { data } = await axios({
    method: 'post',
    url: 'http://localhost:8000/login/',
    data: {
      username: e['username'],
      password:e['password'],
    }
  })
  
  localStorage.clear();
  localStorage.setItem('token', data['token'])
  axios.defaults.headers.common['Authorization'] = `Token ${data['token']}`
  console.log(data['token'])

  return data
}


export const test = async (e:any) => {
  const { data } = await axios({
    method: 'get',
        
    url: 'http://localhost:8000/test/',
  })

  // localStorage.clear();
  // localStorage.setItem('token', data.token)

  console.log(data)

  return data
}

export const getData = async () => {
  const { data } = await axios({
    method: 'get',
        
    url: 'http://localhost:8000/jsondata/',
  })

  return data.data
}
