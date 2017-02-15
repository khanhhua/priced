import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';

import { AppRoutingModule } from './app-routing.module';

import { AlertModule, ModalModule } from 'ng2-bootstrap/ng2-bootstrap';
// Imports for loading & configuring the in-memory web api
//import { InMemoryWebApiModule } from 'angular-in-memory-web-api';
//import { InMemoryDataService }  from './in-memory-data.service';

import { AppComponent } from './app.component';
import { ProductListComponent } from './product-list-component/index';
import { ProductDetailComponent } from './product-detail-component/index';
import { ScenarioListComponent } from './scenario-list-component/index';
import { ScenarioDetailComponent } from './scenario-detail-component/index';
import { TaxcodeListComponent } from './taxcode-list-component/index';
import { TaxcodeDetailComponent } from './taxcode-detail-component/index';
import { ClientSettingsComponent } from './client-settings-component/index';
import { CreateUnitComponent } from './create-unit-component/index';
import { ViewUnitComponent } from './view-unit-component/index';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    //InMemoryWebApiModule.forRoot(InMemoryDataService),
    ModalModule,
    AlertModule,
    AppRoutingModule
  ],
  declarations: [
    AppComponent,
    ProductListComponent,
    ProductDetailComponent,
    TaxcodeListComponent,
    TaxcodeDetailComponent,
    ClientSettingsComponent,
    CreateUnitComponent,
    ViewUnitComponent,
    ScenarioListComponent,
    ScenarioDetailComponent
  ],
  //providers: [ HeroService ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }


/*
Copyright 2016 Google Inc. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/