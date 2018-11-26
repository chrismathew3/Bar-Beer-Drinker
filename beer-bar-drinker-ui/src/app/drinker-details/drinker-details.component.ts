import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DrinkersService, Drinker, Transaction} from '../drinkers.service';
import { HttpResponse } from '@angular/common/http';

declare const Highcharts: any;


@Component({
  selector: 'app-drinker-details',
  templateUrl: './drinker-details.component.html',
  styleUrls: ['./drinker-details.component.css']
})
export class DrinkerDetailsComponent implements OnInit {

  drinkerName: string;
  drinkerDetails: Drinker;
  drinkerTransactions: Transaction[];


  constructor(
    private drinkerService: DrinkersService,
    private route: ActivatedRoute
  ) {
    route.paramMap.subscribe((paramMap) => {

      this.drinkerName = paramMap.get('drinker');

      this.drinkerService.getDrinker(this.drinkerName).subscribe(
        data => {
          this.drinkerDetails = data;
        },
        (error: HttpResponse<any>) => {
          if (error.status === 404) {
            alert('Drinker not found');
          } else {
            console.error(error.status + ' - ' + error.body);
            alert('An error occurred on the server. ');
          }
        }
      );

      this.drinkerService.getTransactions(this.drinkerName).subscribe(
        trans => {
          this.drinkerTransactions = trans;
        },
        (error: HttpResponse<any>) => {
          if (error.status === 404) {
            alert('Transactions not found');
          } else {
            console.error(error.status + ' - ' + error.body);
            alert('An error occured on the server. ');
          }
        }
      );

      this.drinkerService.getBeerCount(this.drinkerName).subscribe(
        data => {
          console.log(data);
          const beers = [];
          const counts = [];
          data.forEach(beer => {
            beers.push(beer.beer);
            counts.push(beer.quantity);
          });
          this.renderChartBC(beers, counts);
        }
      );

      this.drinkerService.getSpending(this.drinkerName).subscribe(
        data => {
          console.log(data);
          const bars = [];
          const counts = [];
          data.forEach(bar => {
            bars.push(bar.bar);
            counts.push(bar.amount);
          });
          this.renderChartSpending(bars, counts);
        }
      );
    });
}
  ngOnInit() { }


  renderChartBC(beers: string[], counts: number[]) {
    Highcharts.chart('bargraph1', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Different beers bought count'
      },
      xAxis: {
        categories: beers,
        title: {
          text: 'Beer'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Quantity'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        beer: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: counts
      }]
    });
  }

  renderChartSpending(bars: string[], counts: number[]) {
    Highcharts.chart('bargraph2', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Spending distribution over various bars'
      },
      xAxis: {
        categories: bars,
        title: {
          text: 'Bar'
        }
      },
      yAxis: {
        min: 0,
        title: {
          text: 'Total Amount'
        },
        labels: {
          overflow: 'justify'
        }
      },
      plotOptions: {
        beer: {
          dataLabels: {
            enabled: true
          }
        }
      },
      legend: {
        enabled: false
      },
      credits: {
        enabled: false
      },
      series: [{
        data: counts
      }]
    });
  }

}
