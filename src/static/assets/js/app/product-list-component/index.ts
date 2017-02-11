import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

import { Http, Response } from '@angular/http';

import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';

import { ModalDirective } from 'ng2-bootstrap/ng2-bootstrap';

import { Product } from "./models";

@Component({
  moduleId: module.id,
  selector: 'priced-product-list',
  templateUrl: './template.html',
  styleUrls: [ './style.css' ]
})
export class ProductListComponent implements OnInit {
  products = [];
  newProduct: Product;

  @ViewChild('newProductModal') public newProductModal:ModalDirective;

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

  onShowNewProductModal(): void {
    console.log(`[onShowNewProductModal]`);

    this.newProduct = {} as Product;
    this.newProductModal.show();
  }

  onSaveNewProduct(product): void {
    const { name } = product;
    this.http.post(`/api/products`, { name })
      .map(res => res.json())
      .subscribe(product => {
        console.log(`[onSaveNewProduct]`, product)

        this.newProductModal.hide();
      })
  }
}