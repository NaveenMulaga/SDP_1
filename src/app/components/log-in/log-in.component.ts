import { AuthService } from './../../auth.service';
import { Component, OnInit } from '@angular/core';
@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit {

  constructor(private _auth: AuthService) { }

  ngOnInit() : void {
  }
 
 

}
