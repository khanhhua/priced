import { Component } from '@angular/core';

@Component({
  selector: 'pr-app',
  template: `<h1>Hello {{name}}</h1>`
})
export class AppComponent { name = 'Angular'; }
