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
  selector: 'priced-create-taxcode',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class CreateTaxcodeComponent implements OnInit {
  taxcode = {} as Taxcode;
  scenarios = [] as [Scenario];

  currentScenario: any = null;
  scenarioResult: any = null;

  constructor (private http: Http,
               private route: ActivatedRoute,
               private router: Router) {}

  ngOnInit () {
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

        this.scenarioResult = result;
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
  
  onSave (): Promise<boolean> {
    const {
      title,
      body,
      effectiveAt: effective_at,
      expiredAt: expired_at
    } = this.taxcode;
    
    this.http.post(`/api/taxcodes`, JSON.stringify(
      {
        title,
        body,
        effective_at,
        expired_at
      }
    )).map(res => {
      const {taxcode} = res.json();
      
      return taxcode as Taxcode;
    }).subscribe(taxcode => {
      console.log(`[onSave] taxcode`, taxcode);
      
      this.router.navigate(['/taxcodes', taxcode.id]);
    });
  }
}

enum ViewMode {

}