import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { Product, Price } from '../models';

@Component({
  moduleId: module.id,
  selector: 'priced-product-detail',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class ProductDetailComponent implements OnInit {
  product: Product = {} as Product;
  newPrice: Price = {} as Price;

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

      this.http.get(`/api/products/${productId}/prices`)
          .map(res => {
            const data = res.json();
            return data.prices as [Price];
          })
          .subscribe(prices => {
            this.product.pricings = Price.fromJSONArray(prices);
          });
    });

  }

  onAddPrice(price) {
    console.log(`[onAddPrice]`, price);

    const {
      effectiveAt: effective_at,
      expiredAt: expired_at,
      value
      } = price;
    this.http.post(`/api/products/${this.product.id}/prices`,
      {
        effective_at,
        expired_at,
        value
      }).map(res => {
        const data = res.json();
        return data.price as Price;
      }).subscribe(price => {
        this.http.get(`/api/products/${this.product.id}/prices`)
          .map(res => {
            const data = res.json();

            return data.prices;
          })
          .subscribe(prices => this.product.pricings = Price.fromJSONArray(prices));
      });
  }
}