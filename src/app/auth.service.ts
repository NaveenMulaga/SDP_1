import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _registerUrl = "http://localhost:3000/api/register";
  constructor(private http: HttpClient) { }
  registerUser(user:"") {​​
    return this.http.post<any>(this._registerUrl, user)
  }​​
 
}
