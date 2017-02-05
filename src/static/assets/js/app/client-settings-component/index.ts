import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';

import { Component, OnInit, ViewChild } from '@angular/core';
import { Router }            from '@angular/router';

import { Unit } from "../models";
import { CreateUnitComponent } from '../create-unit-component/index';

@Component({
  moduleId: module.id,
  selector: 'priced-unit-list',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class ClientSettingsComponent implements OnInit {
  units = [];
  clientIntegration = {
    clientKey: 'HexKeyABC',
    accessCode: 'DEMO0XHEX00000'
  };

  @ViewChild('createUnitModal') private createUnitModal:CreateUnitComponent;
  constructor (private http: Http) {}

  ngOnInit () {
    this.getModel().subscribe(data => this.units = data);
  }

  getModel (): Observable<Unit[]> {
    return this.http.get('/api/units')
      .map(res => {
        const data = res.json();

        return data.units as [Unit];
      });
  }

  viewUnit(unitId: string): void {
    console.log(`[viewUnit] Showing dialog for unit #${unitId}`);

    this.createUnitModal.show();
  }

  createUnit(): void {
    console.log(`[createUnit] Showing dialog for creating unit`);

    this.createUnitModal.show();
  }
}