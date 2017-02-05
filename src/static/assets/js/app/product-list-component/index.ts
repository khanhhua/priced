import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';

import { Component, OnInit } from '@angular/core';
import { Router }            from '@angular/router';
import { Product } from "./models";

@Component({
  moduleId: module.id,
  selector: 'priced-product-list',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class ProductListComponent implements OnInit {
  products = [];

  constructor (private http: Http) {}

  ngOnInit () {
    this.getProducts().subscribe(data => this.products = data);
  }

  getProducts (): Observable<Product[]> {
    return this.http.get('/api/products')
      .map(res => {
        const data = res.json();

        return data.products as [Product];
      });
  }

  viewProduct(productId): void {
    console.log(`[viewProduct] ${productId}`);
  }
}