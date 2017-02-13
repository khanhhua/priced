export class Product {
  id: string;
  name: string;
  kind: string;

  pricings: [Price];
}

export class Price {
  id: string;
  effectiveAt: Date;
  expiredAt: Date;
  createdAt: Date;

  value: number;

  public static fromJSONArray(items) {
    return items.map(item => {
      const {id, effective_at:effectiveAt, expired_at:expiredAt, value} = item;

      return {id, effectiveAt, expiredAt, value} as Price;
    })
  }
}

export class Service {
  id: string;
  name: string;
  kind: string;
}

export class Unit {
  id: string;
  name: string;
  shortForm: string;
}

export class Taxcode {
  id: string;
  created_at: Date;
  effected_on: Date;
  expired_on: Date;

  shared: boolean;
  title: string;
  body: string;
}

export class Client {
  id: string;
  client_key: string;
  access_code: string;
}

export class User {
  id: string;
  roles: [String]
}