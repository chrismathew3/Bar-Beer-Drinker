import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';



export interface Transaction{
  bar: string;
  time: string;
  item: string;
  type: string;
  quantity: string;
  total: string;
  tip: string;
}

export interface Drinker{
  name: string;
  address: string;
  state: string;
  phone: string;
}

@Injectable({
  providedIn: 'root'
})
export class DrinkersService {

  constructor(
    public http: HttpClient
  ) { }

  getDrinkers(){
    return this.http.get<Drinker[]>('/api/drinker');
  }
  getDrinker(drinker: string){
    return this.http.get<Drinker>('/api/drinker/' + drinker);
  }
  getTransactions(drinker: string){
    return this.http.get<Transaction[]>('/api/drinker/transactions/' + drinker);
  }
  getBeerCount(drinker: string){
    return this.http.get<any[]>('/api/drinker/beercount/' + drinker)
  }
  getSpending(drinker: string){
    return this.http.get<any[]>('/api/drinker/spending/' + drinker)
  }

}
