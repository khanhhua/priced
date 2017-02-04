import { Component } from '@angular/core';

@Component({
  moduleId: module.id,
  selector: 'pr-app',
  template: `<router-outlet></router-outlet>`
})
export class AppComponent { name = 'Angular'; }
