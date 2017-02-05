import { Component, ViewContainerRef } from '@angular/core';

@Component({
  moduleId: module.id,
  selector: 'pr-app',
  templateUrl: './app.component.html'
})
export class AppComponent {
  constructor(private viewContainerRef: ViewContainerRef) {}
}
