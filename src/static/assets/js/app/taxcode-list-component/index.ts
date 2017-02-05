import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';

import { Component, OnInit } from '@angular/core';
import { Router }            from '@angular/router';
import { Taxcode } from "../models";

@Component({
  moduleId: module.id,
  selector: 'priced-taxcode-list',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class TaxcodeListComponent implements OnInit {
  taxcodes = [];

  constructor (private http: Http) {}

  ngOnInit () {
    this.getModel().subscribe(data => this.taxcodes = data);
  }

  getModel (): Observable<Taxcode[]> {
    return this.http.get('/api/taxcodes')
      .map(res => {
        const data = res.json();

        return data.taxcodes as [Taxcode];
      });
  }

  viewProduct(productId): void {
    console.log(`[viewProduct] ${productId}`);
  }
}