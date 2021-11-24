import axios from 'axios'
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

export async function axiotTest(e:any) {

  const response = await axios.post(
    'http://localhost:8000/signup/', {
      username: e['username'],
      password:e['password'],
      password2:e['password2'],
    });
    console.log(response);
  
}