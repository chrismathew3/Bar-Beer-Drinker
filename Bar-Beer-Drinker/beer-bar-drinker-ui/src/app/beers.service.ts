import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface Beer{
  name: string;
  type: string;
  manuf: string;
}

@Injectable({
  providedIn: 'root'
})
export class BeersService {

  constructor(
    public http: HttpClient
  ) { }

  getBeers(){
    return this.http.get<Beer[]>('/api/beer');
  }
  getBeer(beer: string){
    return this.http.get<Beer>('/api/beer/' + beer);
  }
  getTopBarsForBeer(beer: string){
    return this.http.get<any[]>('/api/beer/bars/' + beer);
  }
  getTopDrinkersForBeer(beer: string){
    return this.http.get<any[]>('/api/beer/drinkers/' + beer);
  }
}
