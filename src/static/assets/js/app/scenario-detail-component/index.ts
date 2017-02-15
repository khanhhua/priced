import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { Scenario } from '../models';

@Component({
  moduleId: module.id,
  selector: 'priced-scenario-detail',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class ScenarioDetailComponent implements OnInit {
  scenario: Scenario = {} as Scenario;
  
  constructor (private http: Http,
               private route: ActivatedRoute) {}

  ngOnInit () {
    this.route.params.subscribe(params => {
      const scenarioId = params['id'];

      if (!scenarioId) {
        return;
      }

      this.http.get(`/api/scenarios/${scenarioId}`)
          .map(res => {
            const data = res.json();
            return data.scenario as Scenario;
          })
          .subscribe(scenario => this.scenario = scenario);
    });

  }
}