import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { BarsComponent } from './bars/bars.component';

import { HttpClientModule, HttpClient } from '@angular/common/http';
import { TableModule } from 'primeng/table';
import { BarDetailsComponent } from './bar-details/bar-details.component';
import { BeersComponent } from './beers/beers.component';
import { DrinkersComponent } from './drinkers/drinkers.component';
import { DrinkerDetailsComponent } from './drinker-details/drinker-details.component';
import { BeerDetailsComponent } from './beer-details/beer-details.component';
import { GuideComponent } from './guide/guide.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    BarsComponent,
    BarDetailsComponent,
    BeersComponent,
    DrinkersComponent,
    DrinkerDetailsComponent,
    BeerDetailsComponent,
    GuideComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    TableModule,
    HttpClientModule
  ],
  providers: [HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
