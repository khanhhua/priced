import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ProductListComponent } from './product-list-component/index';
import { ProductDetailComponent } from './product-detail-component/index';
import { ScenarioListComponent } from './scenario-list-component/index';
import { ScenarioDetailComponent } from './scenario-detail-component/index';
import { TaxcodeListComponent } from './taxcode-list-component/index';
import { TaxcodeDetailComponent } from './taxcode-detail-component/index';
import { ClientSettingsComponent } from './client-settings-component/index';

const routes: Routes = [
  //{ path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: '', redirectTo: '/products', pathMatch: 'full' },
  //{ path: 'dashboard',  component: DashboardComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent },
  { path: 'scenarios', component: ScenarioListComponent },
  { path: 'scenarios/:id', component: ScenarioDetailComponent },
  { path: 'taxcodes', component: TaxcodeListComponent },
  { path: 'taxcodes/:id', component: TaxcodeDetailComponent },
  { path: 'settings', component: ClientSettingsComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}


/*
Copyright 2016 Google Inc. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/