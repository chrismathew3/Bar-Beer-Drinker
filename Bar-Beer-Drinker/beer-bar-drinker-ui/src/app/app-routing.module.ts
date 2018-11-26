import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { BarsComponent } from './bars/bars.component';
import { BarDetailsComponent } from './bar-details/bar-details.component';
import { BeersComponent } from './beers/beers.component';
import { BeerDetailsComponent } from './beer-details/beer-details.component';
import { DrinkersComponent } from './drinkers/drinkers.component';
import { DrinkerDetailsComponent } from './drinker-details/drinker-details.component';
import { GuideComponent } from './guide/guide.component';


const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'home'
  },
  {
    path: 'static',
    pathMatch: 'full',
    redirectTo: 'home'
  },
  {
    path: 'home',
    pathMatch: 'full',
    component: HomeComponent
  },
  {
    path: 'api/bar',
    pathMatch: 'full',
    component: BarsComponent
  },
  {
    path: 'api/bar/:bar',
    pathMatch: 'full',
    component: BarDetailsComponent
  },
  {
    path: 'api/beer',
    pathMatch: 'full',
    component: BeersComponent
  },
  {
    path: 'api/beer/:beer',
    pathMatch: 'full',
    component: BeerDetailsComponent
  },
  {
    path: 'api/drinker',
    pathMatch: 'full',
    component: DrinkersComponent
  },
  {
    path: 'api/drinker/:drinker',
    pathMatch: 'full',
    component: DrinkerDetailsComponent
  },
  {
    path: 'guide',
    pathMatch: 'full',
    component: GuideComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
