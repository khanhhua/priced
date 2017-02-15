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
  
  createdAt: Date;
}

export class Taxcode {
  id: string;
  createdAt: Date;
  effectiveAt: Date;
  expiredAt: Date;

  shared: boolean;
  title: string;
  body: string;

  public static fromJSON(json: any) {
    const taxcode = new Taxcode();
    const {id,
      created_at: createdAt,
      effective_at: effectiveAt,
      expired_at: expiredAt,
      shared,
      title,
      body} = json;

    taxcode.id = id;
    taxcode.createdAt = createdAt
    taxcode.effectiveAt = effectiveAt
    taxcode.expiredAt = expiredAt;
    taxcode.shared = shared;
    taxcode.title = title;
    taxcode.body = body;

    return taxcode;
  }
}

export class Scenario {
  id: string;
  body: string;
}

export class Client {
  id: string;
  clientKey: string;
  accessCode: string;
}

export class User {
  id: string;
  roles: [String]
}