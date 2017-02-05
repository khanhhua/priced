import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';

import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Taxcode } from "../models";

@Component({
  moduleId: module.id,
  selector: 'priced-taxcode-detail',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class TaxcodeDetailComponent implements OnInit {
  taxcode = {} as Taxcode;

  constructor (private http: Http,
               private route: ActivatedRoute) {}

  ngOnInit () {

    this.route.params.subscribe(params => {
      const taxcodeId = params['id'];

      this.http.get(`/api/taxcodes/${taxcodeId}`)
          .map(res => {
            const data = res.json();

            return data.taxcode as Taxcode;
          })
          .subscribe(taxcode => this.taxcode = taxcode);
    });
  }

  viewProduct(productId): void {
    console.log(`[viewProduct] ${productId}`);
  }
}