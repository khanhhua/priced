import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { Product } from './models';

@Component({
  moduleId: module.id,
  selector: 'priced-product-detail',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class ProductDetailComponent implements OnInit {
  product: Product = {} as Product;

  constructor (private http: Http,
               private route: ActivatedRoute) {}

  ngOnInit () {
    this.route.params.subscribe(params => {
      const productId = params['id'];

      if (!productId) {
        return;
      }

      this.http.get(`/api/products/${productId}`)
          .map(res => {
            const data = res.json();
            return data.product as Product;
          })
          .subscribe(product => this.product = product);
    });

  }
}