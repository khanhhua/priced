import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';
import { Component, Input, Output, ViewChild, OnInit, EventEmitter } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { ModalDirective } from 'ng2-bootstrap/ng2-bootstrap';

import { Unit } from '../models';

@Component({
  moduleId: module.id,
  selector: 'priced-create-unit',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class CreateUnitComponent implements OnInit {
  @Input() name: string;
  @Input() shortForm: string;
  
  @Output() onUnitCreated: EventEmitter = new EventEmitter();

  unit: Unit = {} as Unit;

  @ViewChild('childModal') private childModal:ModalDirective;

  constructor (private http: Http) {}

  ngOnInit () {

  }

  show():void {
    this.name = '';
    this.shortForm = '';

    this.childModal.show();
  }

  onSave():void {
    console.group(`onSave()`);

    this.unit.name = this.name;
    this.unit.shortForm = this.shortForm;

    console.debug(`Unit name:`, this.unit);
    console.groupEnd();
    
    const { name, shortForm:short_form } = this.unit;
    
    this.http.post(`/api/units`, { name, short_form})
        .map(res => {
          const data = res.json();
          
          return data.unit as Unit;
        })
        .subscribe(unit => {
          this.onUnitCreated.emit(unit);
          
          this.childModal.hide();
        });
  }

  onCancel():void {
    this.childModal.hide();
  }
}