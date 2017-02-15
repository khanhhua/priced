import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

import { Http, Response } from '@angular/http';

import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Taxcode, Scenario } from "../models";

@Component({
  moduleId: module.id,
  selector: 'priced-taxcode-detail',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class TaxcodeDetailComponent implements OnInit {
  taxcode = {} as Taxcode;
  scenarios = [] as [Scenario];

  currentScenario: any = null;
  senarioResult: any = null;

  constructor (private http: Http,
               private route: ActivatedRoute) {}

  ngOnInit () {

    this.route.params.subscribe(params => {
      const taxcodeId = params['id'];

      this.http.get(`/api/taxcodes/${taxcodeId}`)
          .map(res => {
            const data = res.json();

            return Taxcode.fromJSON(data.taxcode);
          })
          .subscribe(taxcode => this.taxcode = taxcode);
    });

    this.loadScenarios();
  }

  playScenario(scenarioId:string): void {
    console.log(`[playScenario]`, scenarioId);

    this.currentScenario = new Scenario();

    const data = {
      scenario_id: scenarioId
    };

    this.http.post(`/api/scenario-sessions`, JSON.stringify(data))
      .toPromise()
      .then(res => {
        const result = res.json();

        this.senarioResult = result;
      });
  }

  loadScenarios(): Promise<boolean> {
    console.log(`[loadScenarios] Load scenarios...`);

    this.scenarios = [
      {
        id: 'ID001',
        description: 'Simple model'
      },
      {
        id: 'ID002',
        description: 'Complex model'
      }
    ];
  }
}

enum ViewMode {

}