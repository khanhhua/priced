import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';

import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';

import { ModalDirective } from 'ng2-bootstrap/ng2-bootstrap';

import { Scenario } from "./models";

@Component({
  moduleId: module.id,
  selector: 'priced-scenario-list',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class ScenarioListComponent implements OnInit {
  scenarios = [];
  newScenario: Scenario;

  @ViewChild('newScenarioModal') public newScenarioModal:ModalDirective;

  constructor (private http: Http) {}

  ngOnInit () {
    this.getScenarios().subscribe(data => this.scenarios = data);
  }

  getScenarios (): Observable<Scenario[]> {
    return this.http.get('/api/scenarios')
      .map(res => {
        const data = res.json();

        return data.scenarios as [Scenario];
      });
  }

  onShowNewScenarioModal(): void {
    console.log(`[onShowNewScenarioModal]`);

    this.newScenario = {} as Scenario;
    this.newScenarioModal.show();
  }

  onSaveNewScenario(scenario): void {
    const { title, description, content } = scenario;
    this.http.post(`/api/scenarios`, { title, description, content })
      .map(res => res.json())
      .subscribe(scenario => {
        console.log(`[onSaveNewScenario]`, scenario)

        this.newScenarioModal.hide();
      })
  }
}