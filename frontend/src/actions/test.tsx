import axios from 'axios'
import {v4 as uuidv4} from 'uuid';


let APIURL = "http://host.docker.internal:8000";

export const createuser = async (e:any) => {
    let uuid = uuidv4();
    const { data } = await axios({
      method: 'post',
      url: APIURL + '/signup',
      data: {
        username: uuid,
        password:"",
        password2:"",
      }
    })
    console.log(data)
  
    return data
}
